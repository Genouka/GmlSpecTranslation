import copy
import xml.etree.ElementTree as ET
from translations_part1 import TRANSLATIONS as T1
from translations_part2 import TRANSLATIONS as T2

TRANSLATIONS = {}
TRANSLATIONS.update(T1)
TRANSLATIONS.update(T2)

EN_FILE = 'GmlSpec.en.xml'
ZH_FILE = 'GmlSpec.zh-CN.xml'
OUTPUT_FILE = 'GmlSpec.zh-CN.xml'

def find_child_by_name(parent, tag, name):
    for child in parent.findall(tag):
        if child.get('Name') == name:
            return child
    return None

def translate(text):
    if not text or not text.strip():
        return text
    stripped = text.strip()
    if stripped in TRANSLATIONS:
        zh = TRANSLATIONS[stripped]
        if text.startswith('\n') or text.startswith('\t'):
            return zh
        return zh
    return text

def sync_functions(en_root, zh_root):
    en_funcs = en_root.find('Functions')
    zh_funcs = zh_root.find('Functions')
    if en_funcs is None:
        return 0, 0
    added = 0
    updated = 0
    for en_func in list(en_funcs.findall('Function')):
        name = en_func.get('Name')
        zh_func = find_child_by_name(zh_funcs, 'Function', name)
        if zh_func is None:
            new_func = copy.deepcopy(en_func)
            desc = new_func.find('Description')
            if desc is not None and desc.text:
                desc.text = translate(desc.text)
            for param in new_func.findall('Parameter'):
                if param.text:
                    param.text = translate(param.text)
            zh_funcs.append(new_func)
            added += 1
        else:
            en_desc = en_func.find('Description')
            zh_desc = zh_func.find('Description')
            if en_desc is not None and en_desc.text:
                if zh_desc is None:
                    zh_desc = ET.SubElement(zh_func, 'Description')
                    zh_desc.text = translate(en_desc.text)
                    updated += 1
                elif not zh_desc.text or not zh_desc.text.strip():
                    zh_desc.text = translate(en_desc.text)
                    updated += 1
            for en_param in en_func.findall('Parameter'):
                pname = en_param.get('Name')
                zh_param = find_child_by_name(zh_func, 'Parameter', pname)
                if zh_param is None:
                    new_param = copy.deepcopy(en_param)
                    if new_param.text:
                        new_param.text = translate(new_param.text)
                    zh_func.append(new_param)
                    updated += 1
                elif en_param.text and (not zh_param.text or not zh_param.text.strip()):
                    zh_param.text = translate(en_param.text)
                    updated += 1
    return added, updated

def sync_variables(en_root, zh_root):
    en_vars = en_root.find('Variables')
    zh_vars = zh_root.find('Variables')
    if en_vars is None:
        return 0, 0
    added = 0
    updated = 0
    for en_var in en_vars.findall('Variable'):
        name = en_var.get('Name')
        zh_var = find_child_by_name(zh_vars, 'Variable', name)
        if zh_var is None:
            new_var = copy.deepcopy(en_var)
            if new_var.text:
                new_var.text = translate(new_var.text)
            zh_vars.append(new_var)
            added += 1
        elif en_var.text and (not zh_var.text or not zh_var.text.strip()):
            zh_var.text = translate(en_var.text)
            updated += 1
    return added, updated

def sync_constants(en_root, zh_root):
    en_consts = en_root.find('Constants')
    zh_consts = zh_root.find('Constants')
    if en_consts is None:
        return 0, 0
    added = 0
    updated = 0
    for en_const in en_consts.findall('Constant'):
        name = en_const.get('Name')
        zh_const = find_child_by_name(zh_consts, 'Constant', name)
        if zh_const is None:
            new_const = copy.deepcopy(en_const)
            if new_const.text:
                new_const.text = translate(new_const.text)
            zh_consts.append(new_const)
            added += 1
        elif en_const.text and (not zh_const.text or not zh_const.text.strip()):
            zh_const.text = translate(en_const.text)
            updated += 1
    return added, updated

def sync_structures(en_root, zh_root):
    en_structs = en_root.find('Structures')
    zh_structs = zh_root.find('Structures')
    if en_structs is None:
        return 0, 0
    added = 0
    updated = 0
    for en_struct in en_structs.findall('Structure'):
        sname = en_struct.get('Name')
        zh_struct = find_child_by_name(zh_structs, 'Structure', sname)
        if zh_struct is None:
            new_struct = copy.deepcopy(en_struct)
            for field in new_struct.findall('Field'):
                if field.text:
                    field.text = translate(field.text)
            zh_structs.append(new_struct)
            added += 1
        else:
            for en_field in en_struct.findall('Field'):
                fname = en_field.get('Name')
                zh_field = find_child_by_name(zh_struct, 'Field', fname)
                if zh_field is None:
                    new_field = copy.deepcopy(en_field)
                    if new_field.text:
                        new_field.text = translate(new_field.text)
                    zh_struct.append(new_field)
                    updated += 1
                elif en_field.text and (not zh_field.text or not zh_field.text.strip()):
                    zh_field.text = translate(en_field.text)
                    updated += 1
    return added, updated

def sync_enumerations(en_root, zh_root):
    en_enums = en_root.find('Enumerations')
    zh_enums = zh_root.find('Enumerations')
    if en_enums is None:
        return 0, 0
    added = 0
    updated = 0
    for en_enum in en_enums.findall('Enumeration'):
        ename = en_enum.get('Name')
        zh_enum = find_child_by_name(zh_enums, 'Enumeration', ename)
        if zh_enum is None:
            new_enum = copy.deepcopy(en_enum)
            for member in new_enum.findall('Member'):
                if member.text:
                    member.text = translate(member.text)
            zh_enums.append(new_enum)
            added += 1
        else:
            for en_member in en_enum.findall('Member'):
                mname = en_member.get('Name')
                zh_member = find_child_by_name(zh_enum, 'Member', mname)
                if zh_member is None:
                    new_member = copy.deepcopy(en_member)
                    if new_member.text:
                        new_member.text = translate(new_member.text)
                    zh_enum.append(new_member)
                    updated += 1
                elif en_member.text and (not zh_member.text or not zh_member.text.strip()):
                    zh_member.text = translate(en_member.text)
                    updated += 1
    return added, updated

def indent_xml(elem, level=0):
    indent = "\n" + "\t" * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent

def main():
    print("Parsing English XML...")
    en_tree = ET.parse(EN_FILE)
    en_root = en_tree.getroot()

    print("Parsing Chinese XML...")
    zh_tree = ET.parse(ZH_FILE)
    zh_root = zh_tree.getroot()

    print(f"Translation dictionary size: {len(TRANSLATIONS)}")

    total_added = 0
    total_updated = 0

    print("\n=== Syncing Functions ===")
    a, u = sync_functions(en_root, zh_root)
    total_added += a
    total_updated += u
    print(f"  Added: {a}, Updated: {u}")

    print("\n=== Syncing Variables ===")
    a, u = sync_variables(en_root, zh_root)
    total_added += a
    total_updated += u
    print(f"  Added: {a}, Updated: {u}")

    print("\n=== Syncing Constants ===")
    a, u = sync_constants(en_root, zh_root)
    total_added += a
    total_updated += u
    print(f"  Added: {a}, Updated: {u}")

    print("\n=== Syncing Structures ===")
    a, u = sync_structures(en_root, zh_root)
    total_added += a
    total_updated += u
    print(f"  Added: {a}, Updated: {u}")

    print("\n=== Syncing Enumerations ===")
    a, u = sync_enumerations(en_root, zh_root)
    total_added += a
    total_updated += u
    print(f"  Added: {a}, Updated: {u}")

    print(f"\n=== TOTAL: Added={total_added}, Updated={total_updated} ===")

    indent_xml(zh_root)

    print(f"\nSaving to {OUTPUT_FILE}...")
    zh_tree.write(OUTPUT_FILE, encoding='utf-8', xml_declaration=True)

    with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("<?xml version='1.0' encoding='utf-8'?>", '<?xml version="1.0" encoding="UTF-8"?>')
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done!")

if __name__ == '__main__':
    main()
