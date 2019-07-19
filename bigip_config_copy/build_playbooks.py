import json

print "- name: Base VE config"
print "  hosts: \"{{ target_hosts | default('f5') }}\""
print "  connection: local"
print "  gather_facts: False"

print "  vars:"
print "    bigip_provider:"
print "      server: 10.1.1.245"
print "      user: admin"
print "      password: admin"
print "      validate_certs: no"
print "    new_bigip:"
print "      server: 10.1.1.246"
print "      user: admin"
print "      password: admin"
print "      validate_certs: no"

print "  tasks:"
print "  - name: jam nodes in"
print "    bigip_node:"
print "      state: present"
print "      name: \"{{ item.name }}\""
print "      address: \"{{ item.address }}\""
print "      connection_limit: \"{{ item.connection_limit }}\""
print "      dynamic_ratio: \"{{ item.dynamic_ratio }}\""
print "      rate_limit: \"{{ item.rate_limit }}\""
print "      ratio: \"{{ item.ratio }}\""
print "      provider: \"{{ new_bigip }}\""
print "    delegate_to: localhost"
print "    with_items: "


with open('nodes.json') as json_file:
    data = json.load(json_file)
    for p in data['nodes']:
        address = str(p['address'])
        conn_limit = int(p['connection_limit'])
	dynamic_ratio = int(p['dynamic_ratio'])
        name = str(p['name'])
	rate_limit = int(p['rate_limit'])
        ratio = int(p['ratio'])

 	print "      - name: " + name
 	print "        address: " + address
 	print "        connection_limit: ", conn_limit
 	print "        dynamic_ratio: ", dynamic_ratio
 	print "        rate_limit: ", rate_limit
 	print "        ratio: ", ratio
json_file.close()

print "  - name: jam pools in"
print "    bigip_pool:"
print "      state: present"
print "      name: \"{{ item.name }}\""
print "      lb_method: \"{{ item.lb_method }}\""
print "      provider: \"{{ new_bigip }}\""
print "      monitors: \"{{ item.monitors }}\""
print "    delegate_to: localhost"
print "    with_items: "


with open('pools.json') as json_file:
    data = json.load(json_file)
    for p in data['ltm_pools']:
        name = str(p['name'])
        lb_method = str(p['lb_method'])
 	print "      - name: " + name
        print "        lb_method: " + lb_method
        print "        monitors: "
        for monitor in p['monitors']:
          print "          - " + monitor
json_file.close()


print "  - name: jam pools members in"
print "    bigip_pool_member:"
print "      state: present"
print "      pool: \"{{ item.name }}\""
print "      address: \"{{ item.address }}\""
print "      port: \"{{ item.port }}\""
print "      provider: \"{{ new_bigip }}\""
print "    delegate_to: localhost"
print "    with_items: "


# add pool members
with open('pools.json') as json_file:
    data = json.load(json_file)
    for p in data['ltm_pools']:
        for member in p['members']:
          name = str(p['name'])
          member_address = str(member['address'])
          dynamic_ration = int(member['dynamic_ratio'])
          fqdn_autopopulate = str(member['fqdn_autopopulate'])
          inherit_profile = str(member['inherit_profile'])
          logging = str(member['logging'])
          member_name = str(member['name'])
          priority_group = int(member['priority_group'])
          rate_limit = str(member['rate_limit'])
          ratio = int(member['ratio'])
          full_path = str(member['full_path'])
          just_port = full_path.split(":")

 	  print "      - name: " + name
          print "        lb_method: " + lb_method
          print "        address: " + member_address
          print "        dynamic_ration: ", dynamic_ratio
          print "        fqdn_autopopulate: " + fqdn_autopopulate
          print "        inherit_profile: " + inherit_profile
          print "        logging: " + logging
          print "        member_name: " + member_name
          print "        priority_group: ", priority_group
          print "        rate_limit: ", rate_limit
          print "        ratio: ", ratio
          print "        port: " + just_port[1]

json_file.close()


print "  - name: jam virtual servers in"
print "    bigip_virtual_server:"
print "      state: present"
print "      name: \"{{ item.name }}\""
print "      mirror: \"{{ item.connection_mirror_enabled }}\""
print "      pool: \"{{ item.pool }}\"" 
print "      description: \"{{ item.description }}\""
print "      destination: \"{{ item.destination_address }}\""
print "      port: \"{{ item.destination_port }}\""
print "      ip_protocol: \"{{ item.protocol }}\""
print "      rate_limit: \"{{ item.rate_limit }}\""
print "      rate_limit_dst_mask: \"{{ item.rate_limit_dst_mask }}\""
print "      rate_limit_mode: \"{{ item.rate_limit_mode }}\""
print "      rate_limit_src_mask: \"{{ item.rate_limitsrc_mask }}\""
print "      port_translation: \"{{ item.translate_port }}\""
print "      snat: \"{{ item.snat_type }}\""
print "      source: \"{{ item.source }}\""
print "      source_port: \"{{ item.source_port_behavior }}\"" 
print "      type: \"{{ item.type }}\""
print "      provider: \"{{ new_bigip }}\""
print "    delegate_to: localhost"
print "    with_items: "


# add virtuals
with open('virtual.json') as json_file:
    data = json.load(json_file)
    for virt in data['virtual_servers']:
      name = str(virt['name'])
      connection_mirror_enabled = str(virt['connection_mirror_enabled'])
      pool = str(virt['default_pool'])
      description = str(virt['description'])
      destination_address = str(virt['destination_address'])
      destination_port = str(virt['destination_port'])
      protocol = str(virt['protocol'])
      rate_limit = int(virt['rate_limit'])
      if rate_limit < 0:
        rate_limit = 0
      rate_limit_dst_mask = int(virt['rate_limit_destination_mask'])
      rate_limit_mode = str(virt['rate_limit_mode'])
      rate_limitsrc_mask = int(virt['rate_limit_source_mask'])
      snat_type = str(virt['snat_type'])
      translate_port = str(virt['translate_port'])
      source = str(virt['source_address'])
      source_port_behavior = str(virt['source_port_behavior'])
      type = str(virt['type'])

      print "      - name: " + name
      print "        connection_mirror_enabled: " + connection_mirror_enabled
      print "        pool: " + pool
      print "        description: " + description
      print "        destination_address: " + destination_address
      print "        destination_port: " + destination_port
      print "        protocol: " + protocol
      print "        rate_limit: ", rate_limit
      print "        rate_limit_dst_mask: ", rate_limit_dst_mask
      print "        rate_limit_mode: " + rate_limit_mode
      print "        rate_limitsrc_mask: ", rate_limitsrc_mask
      print "        snat_type: " + snat_type
      print "        source: " + source
      print "        source_port_behavior: " + source_port_behavior
      print "        translate_port: " + translate_port
      print "        type: " + type
