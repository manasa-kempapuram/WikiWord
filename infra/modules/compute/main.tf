resource "aws_instance" "this" {
  count         = var.instance_count
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = element(var.subnet_ids, count.index % length(var.subnet_ids))

  key_name = var.key_name

  tags = merge(var.tags, {
    Name = "${var.instance_name}-${count.index + 1}"
  })
}
