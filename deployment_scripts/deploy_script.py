# Filename: deploy_script.py
# Author: Eke
# Date: March 4, 2024
# Description: This Python script simulates a basic deployment process by printing deployment steps.



def deploy_application(environment, version):
    # Simulate the deployment process
    print(f"Deploying version {version} to {environment} environment... ")
    print("Updating configuration files...")
    print("Restarting application servers...")
    print("Deployment completed successfully!")


def main():
    # Main function to execute the deployment simulation
    print("Welcome to the Deployment Simulator!")

    # Get the user input for deployment parameters
    env = input("Enter deployment environment (e.g. dev, staging, prod): ")
    version = input("Enter version to deploy: ")

    # Deploy the application
    deploy_application(environment=env, version=version)

if __name__ == "__main__":
    main()