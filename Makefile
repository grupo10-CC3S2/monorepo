tf-init:
	terraform -chdir=environments/terraform init

tf-plan:
	terraform -chdir=environments/terraform plan

tf-apply:
	terraform -chdir=environments/terraform apply

tf-aa:
	terraform -chdir=environments/terraform apply -auto-approve

tf-da:
	terraform -chdir=environments/terraform destroy -auto-approve

tf-test:
	terraform init
	terraform test

tf-clean:
	rm -rf environments/terraform/.terraform
	rm -f environments/terraform/.terraform.lock.hcl
	rm -f environments/terraform/terraform.tfstate*