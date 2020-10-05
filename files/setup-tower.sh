# create projects
tower-cli project create --name ansible --scm-type git --scm-url http://github.com/codecowboydotio/ansible --organization Default --wait

echo "Waiting for repos to sync"
#./spinner.sh sleep 45


# Create credentials
tower-cli credential create --name bigip-ssh --organization Default --credential-type Machine --inputs='{"username":"root","password":"default"}'
tower-cli credential create --name root-ssh --organization Default --credential-type Machine
tower-cli credential create --name "aws-account" --organization Default --credential-type "Amazon Web Services" --inputs='{"username":"aaa","password":"AAA"}'

# create inventories
tower-cli inventory create --name localhost --organization Default
tower-cli host create --name localhost --inventory localhost
tower-cli inventory create --name bigip --organization Default
tower-cli host create --name 10.1.1.245 --inventory bigip
tower-cli inventory create --name AWS --organization Default
tower-cli inventory_source create --name "aws-source" --inventory "AWS" --source ec2 --credential "aws-account" --update-on-launch "true" --overwrite "true" --instance-filters "tag:application=build"

# create job templates
tower-cli job_template create --name "New Server" --job-type run --inventory localhost --project ansible --playbook pacman.yml --credential root-ssh --ask-variables-on-launch "true" --extra-vars "target_hosts=all"
tower-cli job_template associate_credential --credential aws-account --job-template "New Server"

tower-cli job_template create --name "Install Application" --job-type run --inventory AWS --project ansible --playbook pacman2.yml --credential root-ssh --extra-vars "target_hosts=all"

tower-cli job_template create --name "Update Tags" --job-type run --inventory AWS --project ansible --playbook pacman3.yml --credential root-ssh --extra-vars "target_hosts=all"
tower-cli job_template associate_credential --credential aws-account --job-template "Update Tags"

#create workflow
tower-cli workflow create --name "webapp_workflow"
sleep 10
#tower-cli workflow schema webapp_workflow @pacman_workflow.yml

# delete default stuff
tower-cli job_template delete --name "Demo Job Template"
#tower-cli project delete --name "Demo Project"
tower-cli credential delete --name "Demo Credential"
tower-cli inventory delete --name "Demo Inventory"
