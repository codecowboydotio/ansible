when CLIENT_ACCEPTED {

   # Trigger a name lookup for new connections
   set do_lookup 1
   set irule_debug 1
   if { $irule_debug equals 1 } {   
       log local0. "[IP::client_addr]:[TCP::client_port]: New connection to [IP::local_addr]:[TCP::local_port]"
   }    
}
when HTTP_REQUEST {

   # Check if we haven't done a lookup already on this connection
   if { $do_lookup }{
	  if { $irule_debug equals 1 } {   
        log local0. "[IP::client_addr]:[TCP::client_port]: Collecting HTTP for new lookup"
      }
      # Hold HTTP data until client IP address is resolved
      HTTP::collect

      #  Start a name resolution on the client IP address
      NAME::lookup -ptr [IP::client_addr]
   }
}

when NAME_RESOLVED {

   # FQDN of client IP address
   set ptr [string tolower [NAME::response]]
   set ptr "owa.wired.com" 
   if { $irule_debug equals 1 } {    
     log local0. "[IP::client_addr]:[TCP::client_port]: Lookup result: $ptr"
   }
   if { [class match $ptr contains foo_dg]} {
	  HTTP::respond 403 content "You are on the list\r\n"
	  TCP::close  
   }  else {
	HTTP::release
	set do_lookup 0
   }
}

