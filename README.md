# OCI Data Integration Terraform Examples

This repository contains sample terraform scripts for OCI Data Integration.

Example
1. cd import
2. change the values in the file terraform.tfvars.example for your environment, you will need;
   * Tenancy ocid for object storage export file = "ocid1.tenancy.oc..."
   * Region              = "us-ashburn-1"
   * Compartment ocid to create the workspace = "ocid1.compartment.oc1......"
   * Workspace display name to create = "DIS Reference Architecture v0.1"
   * Workspace is private network enabled = "true"
   * Workspace subnet id = "ocid1.subnet.oc1....................."
   * Workspace vcn_id = "ocid1.vcn.oc1.phx......................."
   * Bucket name where the export ZIP has been placed
   * File name of the export file
3. terraform init
4. terraform plan
5. terraform apply

This will take a few minutes to create the workspace and then import your content!

