def validate_text(dialog_text: str) -> bool:
    output: bool = False
    if (dialog_text.lower().isdigit() == True or
            dialog_text.lower() == "" or 
            dialog_text.lower().isspace() == True):
        output = False
    else:
        output = True
    return output


def validate_comp(label: str, list_count: int) -> bool:
    output: bool = True
    if (label.lower() != "placeholder" and
            list_count > 0):
        output = False
    else:
        output = True
    return output
