import os, sys;
import yaml;

def getprop(doc, name):
    if name not in doc: 
        print("could not find property: {}\n".format(name));
        sys.exit();
    else: 
        return doc[name];

def parsemember(doc, name):
    if name == "struct" or name == "func":
        prop1 = getprop(doc, "type");
        prop2 = getprop(doc, "name");
        out  = "   {}, {}\n".format(prop1, prop2);
    else:
        prop1 = getprop(doc, "name");
        prop2 = getprop(doc, "value");
        out = "   {}, {}\n".format(prop1, prop2);
    return out, len(prop1), len(prop2) if type(prop2) is not int else 1;

def decltype(name):
    decls = {"func": "Parameter", "struct": "Member", "enum": "Enum"}
    return decls[name];

def parsedecl(doc, name):
    out  = "{}: {}\n{}\n".format(name[0], getprop(doc, "id"), "=" * (len(doc["id"]) + 3));
    out += "{}\n\n".format(getprop(doc, "name"));
    out += "Description\n{}\n{}\n".format("-" * len("Description"), getprop(doc, "desc"));
    out += "{}s\n{}\n\n".format(decltype(name), "-" * (len(decltype(name)) + 1));
    out += ".. csv-table::\n";
    out += "   :widths: $$width$$, $$height$$\n\n";
    
    lenmax1 = lenmax2 = 0;
    for _, comp in getprop(doc, "comp").items():
        (outstr, len1, len2) = parsemember(comp, name);
        out += outstr;
        lenmax1 = max(len1, lenmax1);
        lenmax2 = max(len2, lenmax2);

    out = out.replace("$$width$$", str(lenmax1), 1);
    out = out.replace("$$height$$", str(lenmax2), 1);
    
    out += "\n\n----\n\n";
    return out;

def parsefile(doc):
    out  = ".. File: {}\n".format(doc["file"]);
    out += ".. This file is autogenerated. Do not edit.\n\n";

    props = ["enum", "struct", "func"];

    for p in props:
        if p in doc:
            for _, decl in doc[p].items():
                out += parsedecl(decl, p);
    
    out += ".. Footer";

    return out;

def main():
    doc = None;
    with open(sys.argv[1]) as f:
        doc = yaml.load(f, yaml.FullLoader);
        print(doc);

    with open(sys.argv[2], "w") as f:
        out = parsefile(doc); 
        f.write(out);

if __name__ == "__main__":
    main();
