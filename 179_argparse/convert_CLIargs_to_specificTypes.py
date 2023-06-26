import argparse
import pathlib

def get_absolute_path(argument: str) -> pathlib.Path:
    return pathlib.Path(argument).absolute()

def get_parser() -> argparse.ArgumentParser:
    _parser = argparse.ArgumentParser()
    # _parser.add_argument("document_path") # python .\convert_CLIargs_to_specificTypes.py .\file.txt
    # _parser.add_argument("document_path", type=int) # python .\convert_CLIargs_to_specificTypes.py 42
    # _parser.add_argument("document_path", type=pathlib.Path) # python .\convert_CLIargs_to_specificTypes.py .\file.txt
    _parser.add_argument("document_path", type=get_absolute_path)
    return _parser

def process_document(document_path: pathlib.Path) -> None: #returns nothing
    print(type(document_path))
    print(document_path)

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    process_document(args.document_path)


