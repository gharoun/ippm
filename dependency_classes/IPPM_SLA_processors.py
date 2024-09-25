import re


class IPPMSLAProcessor:

    @staticmethod
    def process_ippm_section(ippm_dict):
        new_ippm = []
        for key, line in ippm_dict.items():  # Iterate over key-value pairs
            if line.strip().startswith('session'):
                before_name = line.split('name')[0]
                after_source = line.split('source')[-1]
                modified_line = re.sub(
                    r'[^a-zA-Z0-9_]', '', line.split('name ')[-1].split(' source')[
                        0].replace(' ', '_')
                )

                # Append the modified line
                new_ippm.append(
                    f" {before_name}name {modified_line} source{after_source}")

        return new_ippm

    @staticmethod
    def delete_ippm(ippm_dict):
        del_ippm = ["context local", "ippm twamp light cont-sender ",]
        for key, line in ippm_dict.items():
            if line.strip().startswith('session'):
                del_ippm.append(f" no session {key}")
        return del_ippm

    @staticmethod
    def proccess_SLA_jobs(ippm_dict):
        new_sla = []
        for key, line in ippm_dict.items():
            if line.strip().startswith('session'):
                new_sla.append(
                    f"sla job {key}\n type twamp\n  session {key} context local\n enable")
        return new_sla

    @staticmethod
    def append_to_file(lines, output_path):
        with open(output_path, 'a', encoding="utf-8") as output_file:
            for line in lines:
                output_file.write(line + "\n")
