import os
import tornado.web

class ViewLoader(tornado.template.DictLoader):
    def __init__(self, root_dir: str, autoescape = "xhtml_escape"):
        # recursively compile a compendium of all templates
        template_book = {}
        def compile_templates(dir):
            # for every node in the directory
            for node in os.listdir(dir):
                # get its real path
                real_node = os.path.abspath(os.path.join(dir, node))
                # if it is a directory
                if os.path.isdir(real_node):
                    # recurse
                    compile_templates(real_node)
                # otherwise
                elif os.path.isfile(real_node):
                    # get relative path to node without extension to use as predictable name
                    node = os.path.splitext(os.path.relpath(real_node, root_dir))[0]
                    # read into template book
                    with open(real_node, "r") as fp:
                        template_book[node] = fp.read()
        compile_templates(root_dir)
        # initialize dictloader
        super().__init__(template_book)
    def resolve_path(self, name: str, parent_path: str = None) -> str:
        return name