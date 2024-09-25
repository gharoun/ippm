class SectionExtractor:
    def __init__(self, input_file, start_line, end_line):
        self.lines = self.__read_input_to_list(input_file)
        self.__start_marker = start_line
        self.__end_marker = end_line

    def __read_input_to_list(self, input_file):
        try:
            with open(input_file, 'r', encoding="utf-8") as f:
                lines = [line.strip() for line in f.readlines()]
            return lines
        except FileNotFoundError:
            print(f"Error: The file {input_file} was not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def __extract_section(self, lines, start_marker, end_marker):
        section_lines = {}
        in_section = False
        for line in lines:
            if start_marker in line:
                in_section = True

            if in_section:
                parts = line.split()
                if len(parts) > 1:  # Ensure there are enough parts to avoid IndexError
                    session_number = parts[1]
                    section_lines[session_number] = line.strip()

            if in_section and end_marker in line:
                break

        return section_lines

    def get_extracted_lines_decs(self):
        return self.__extract_section(self.lines, self.__start_marker, self.__end_marker)
