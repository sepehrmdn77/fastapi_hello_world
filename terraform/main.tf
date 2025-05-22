module "EC2_instance" {
  source       = "./module/EC2_instance"
  key_name     = "key_pair_name"  # key pair name here wothout .pem
  machine_name = "instance name"  # instance name that you want to create through the module
}