variable "ami" {
  default     = "ami-0a94c8e4ca2674d5a"  # default value of ami
  type        = string
  description = "This is the machine ami"
}
variable "instance_type" {
  default = "t2.micro"  # default instance type
}
variable "key_name" {}
variable "machine_name" {}