def extract_rules(file):
    rules = set()
    for line in file:
        rule = line.strip()
        if not rule:
            break
        rules.add(tuple([int(i) for i in line.split('|')]))
    f.seek(0)
    return rules

def is_ordered(pages, rules):
    for page in pages:
        for i, j in rules:
            if i == page and j in pages and (pages.index(i) > pages.index(j)):
                return False
    return True

def order_pages(pages, rules):
    ordered_pages = [None] * len(pages)
    others = set()
    for page in pages:
        count = 0
        for i, j in rules:
            if i == page and j in pages:
                count += 1
        if count:
            ordered_pages[-1 * (count + 1)] = page
        else:
            others.add(page)

    for page in others:
        idx = ordered_pages.index(None)
        ordered_pages[idx] = page
    return ordered_pages

def part1(file):
    rules = extract_rules(file)
    updates = False

    total_sum = 0
    for line in file:
        pages = line.strip()
        if not pages:
            updates = True
            continue

        if updates:
            pages = [int(page) for page in pages.split(',')]
            if is_ordered(pages, rules):
                total_sum += pages[(len(pages) - 1) // 2]
    return total_sum

def part2(file):
    rules = extract_rules(file)
    updates = False
    
    total_sum = 0
    for line in file:
        pages = line.strip()
        if not pages:
            updates = True
            continue

        if updates:
            pages = [int(page) for page in pages.split(',')]
            if not is_ordered(pages, rules):
                pages = order_pages(pages, rules)
                total_sum += pages[(len(pages) - 1) // 2]
    return total_sum

if __name__ == '__main__':
    with open('day5_input.txt', 'r') as f:
        print(part1(f))
    with open('day5_input.txt', 'r') as f:
        print(part2(f))