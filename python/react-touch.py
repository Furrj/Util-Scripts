#!/usr/bin/env python3

import sys
import os

if __name__ == "__main__":
    filename = ""
    path = ""
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        path = filename
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        path = f"{sys.argv[2]}/{filename}"
    else:
        exit("Error: Incorrect number of arguments")

    # create folder
    print(path)
    os.makedirs(path)

    # create tsx
    f = open(f"{path}/{filename}.tsx", "w")
    # write to tsx
    tsx_file_content = f'import styles from "./{filename}.module.scss";\n\n'
    tsx_file_content += f"const {filename}: React.FC = () => \u007b\n"
    tsx_file_content += f'\treturn <div className={"{styles.root}"}>{filename}</div>;\n'
    tsx_file_content += "};\n\n"
    tsx_file_content += f"export default {filename};"
    f.write(tsx_file_content)
    f.close()

    # create scss module
    f = open(f"{path}/{filename}.module.scss", "w")
    # write to scss module
    scss_file_content = ".root {\n"
    scss_file_content += "}"
    f.write(scss_file_content)
    f.close()
