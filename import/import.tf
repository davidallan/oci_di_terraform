locals {
  python = (substr(pathexpand("~"), 0, 1) == "/") ? "python3" : "python.exe"
}

resource "null_resource" "import_objects" {
  depends_on = [ oci_dataintegration_workspace.dis_workspace ]

    provisioner "local-exec" {
    command = <<EOT
python3 scripts/import.py ${oci_dataintegration_workspace.dis_workspace.id} ${var.bucket_name} ${var.file_name} ${var.tenancy_ocid} ${var.region} ${var.principal}
EOT
    working_dir = "${path.module}"
    interpreter = [
      "/bin/bash", "-c"
    ]
  }

}
