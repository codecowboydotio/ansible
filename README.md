# ansible

This is a place for me to put my ansible scripts.
I'm slowly converting everything to be role based rather than monolithic script based.

# Bitcoin role:

This role pulls bitcoin from github, compiles the source.
It chooses the OS that it compiles on (at this point it understands yum and apt).
I chose to use the ansible_pkg_mgr directive because it allows me to compile for different "types" or operating systems.
If I chose to use the ansible_os_family then I would need to write more plays for more operating systems.
A case in point here is my raspberry pi. Using the ansible_pkg_mgr I can have one play that covers "debian like" systems
that use apt as a package manager instead of one for "debian like" and one for "raspberry pi".

#Sawtooth:

This role pulls sawtooth lake

- validator
- core
- marketplace

and builds them all on the one box.

It is intended for testing, where you want to test OUTSIDE of the vagrant ubuntu images that are supplied.

#eap70:

This role installs a version of JBoss EAP 7.0 (wildfly) and sets a password.

#eap649:

This role installs a version of JBoss EAP 649 and patches. It is suitable for use with JBoss BPM suite (or other applications)


