# fastapi_hello_world
Simple hello world with fastapi

# plan
Before deploying the project do not forget to export credentials in case of security matters.
$ export AWS_ACCESS_KEY_ID="anaccesskey"
$ export AWS_SECRET_ACCESS_KEY="asecretkey"
$ terraform plan

# user and domain
The instance user is ubuntu by default but if you are using another system type or have another user you have to change 'ubuntu' in ansible/roles, ansible/ansible.cfg, docker-compose and the domain has to be inserted in the docker-compose in traefik router section to connect the instance to the domain.

# key_pair_name
after deploying instance with terrafrom apply you have to change the instance ip in ansible/hosts