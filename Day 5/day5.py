def extract_rules(filename):
    with open(filename, 'r') as f:
        rules = set()
        for line in f:
            rule = line.strip()
            if not rule:
                break
            rules.add(tuple([int(i) for i in line.split('|')]))
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

rules = extract_rules('day5_input.txt')
updates = False

with open('day5_input.txt', 'r') as f:
    total_sum = 0
    for line in f:
        pages = line.strip()
        if not pages:
            updates = True
            continue

        if updates:
            pages = [int(page) for page in pages.split(',')]
            if not is_ordered(pages, rules):
                pages = order_pages(pages, rules)
                total_sum += pages[(len(pages) - 1) // 2]

# with open('day5_input.txt', 'r') as f:
#     total_sum = 0
#     for line in f:
#         pages = line.strip()
#         if not pages:
#             updates = True
#             continue

#         if updates:
#             pages = [int(page) for page in pages.split(',')]
#             if is_ordered(pages, rules):
#                 total_sum += pages[(len(pages) - 1) // 2]

print(total_sum)