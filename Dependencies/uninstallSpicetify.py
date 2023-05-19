import subprocess

def run_powershell_commands(commands):
    try:
        # Run PowerShell as a subprocess
        process = subprocess.Popen(
            ["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command", "& {" + commands + "}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Get the output and error messages, if any
        output, error = process.communicate()

        # Check for any errors
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, "PowerShell Error", error)
        
        # Return the output as a string
        return output

    except subprocess.CalledProcessError as e:
        print("Error executing PowerShell commands:", e)

# Specify the PowerShell commands to run
commands = r"spicetify unapply; spicetify restore; spicetify backup remove"

# Run the PowerShell commands
output = run_powershell_commands(commands)

# Print the output
print("Output:\n", output)
