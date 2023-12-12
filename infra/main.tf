locals{
  key_value = "devops"
}

resource "aws_instance" "demo" {
  ami           = "ami-0287a05f0ef0e9d9a"
  instance_type = "t2.micro"
  key_name = local.key_value
  vpc_security_group_ids = ["sg-0be4b1c481224649d"]

  tags = {
    Name = "Kaushik_mass"
  }
}