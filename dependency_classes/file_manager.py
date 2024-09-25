import os
import sys


class FileManager:
    def __init__(self, output_name: str = "formatted_ippm.txt", output_dir: str = "."):
        """Initialize FileManager with output name and directory."""
        self.__output_name = output_name
        self.__output_dir = os.path.expanduser(os.path.expandvars(output_dir))
        self.__output_path = os.path.join(
            self.__output_dir, self.__output_name)

    def check_number_argument(self):
        """Check the number of arguments after the script."""
        if len(sys.argv) < 2:
            print("No input file provided. You will be prompted to enter one.")
            # Call the method to get a valid file path
            input_file = self.__check_file_exists()
            return input_file
        else:
            input_file = sys.argv[1]
            if not os.path.isfile(input_file):
                print(f"Input file '{input_file}' not found.")
                input_file = self.__check_file_exists()
        return input_file

    def __check_file_exists(self):
        """Prompt the user to enter a valid input file path until it exists."""
        count = 0
        while count < 5:
            file_path = input("Enter the input file path: ")
            if os.path.isfile(file_path):
                print(f"Input file '{file_path}' found.")
                return file_path  # Return the valid file path
            else:
                print(f"Error: Input file '{
                      file_path}' not found. Please try again.")
                count += 1
        self.print_to_many_tries()

    def set_output_file_name(self):
        """Prompt user for output file name."""
        output_name = input(
            f"Enter output file name (default: {self.__output_name}): ")
        self.__output_name = output_name or self.__output_name
        self.__update_output_path()

    def set_output_directory(self):
        """Prompt user for output directory."""
        count = 0
        while count < 5:  # Loop up to 5 times
            dir_path = input(f"Enter directory to save the file (default: {
                             self.__output_dir}): ") or self.__output_dir

            # Expand user home and environment variables
            expanded_path = os.path.expanduser(os.path.expandvars(dir_path))

            if os.path.isdir(expanded_path):
                self.__output_dir = expanded_path
                self.__update_output_path()  # Update the output path based on the new directory
                print(f"Output directory set to: {self.__output_dir}")
                break
            else:
                print(f"Error: Directory '{
                      dir_path}' does not exist. Please try again.")
                count += 1

        if count == 5:
            self.print_to_many_tries()

    def handle_existing_file(self):
        """Handle scenarios where the output file already exists."""
        if os.path.isfile(self.__output_path):
            print(f"The file '{self.__output_path}' already exists.")
            count = 0
            while count < 5:  # Allow up to 5 attempts
                choice = input(
                    "Choose an option:\n1) Replace it\n2) Alter the name\n3) Exit\nEnter your choice (1, 2, or 3): "
                )

                if choice == '1':
                    print(f"Replacing '{self.__output_path}'.")
                    os.remove(self.__output_path)
                    break  # Exit the loop after replacing
                elif choice == '2':
                    new_output_file = input(
                        "Enter a new output file name: ") or "formatted_ippm.txt"
                    if new_output_file == self.__output_name:
                        print("This file already exists! Please try again!")
                    else:
                        self.__output_name = new_output_file
                        self.__update_output_path()
                        break  # Exit the loop after updating the name
                elif choice == '3':
                    print("Exiting the file handling process.")
                    sys.exit(1)
                else:
                    print("Invalid option. Please choose 1, 2, or 3.")
                    count += 1
            if count == 5:
                self.print_to_many_tries()

    def get_output_path(self):
        """Public method to retrieve the output path."""
        return self.__output_path

    def __update_output_path(self):
        """Update the output file path based on the current output name and directory."""
        self.__output_path = os.path.join(
            self.__output_dir, self.__output_name)
        print(f"Output path updated to: {self.__output_path}")

    @staticmethod
    def print_to_many_tries():
        """Private method to handle too many attempts."""
        print("-" * 65)
        print("Maximum attempts reached. Please contact gaya.haroun@viaero.com")
        print("-" * 65)
        sys.exit(1)
