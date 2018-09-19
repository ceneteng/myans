provider "aws" {
  region     = "us-east-1"
}

variable "vpc_id" {}

data "aws_vpc" "TestVPC" {
    id = "${var.vpc_id}"
}
resource "aws_security_group" "TestALB" {
  name        = "ALB"
  description = "sg for load balancer"
  vpc_id      = "${data.aws_vpc.TestVPC.id}"
}

resource "aws_security_group" "TestBastion" {
  name        = "TestBastion"
  description = "sg for Bastion"
  vpc_id      = "${data.aws_vpc.TestVPC.id}"
}

resource "aws_security_group" "TestWP" {
  name        = "TestWP"
  description = "sg for WordPress"
  vpc_id      = "${data.aws_vpc.TestVPC.id}"
}