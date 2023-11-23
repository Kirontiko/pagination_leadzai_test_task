def add_pages(pages: list, start: int, end: int) -> list:
    pages.extend(range(start, end + 1))
    return pages


def paginate(current_page: int,
             total_pages: int,
             boundaries: int,
             around: int) -> str:
    args = [current_page, total_pages, boundaries, around]
    if not all(isinstance(arg, int) for arg in args):
        raise TypeError("All arguments must be integers.")

    if not all(arg >= 0 for arg in args):
        raise ValueError("All arguments must be positive integers")

    if boundaries < 0:
        raise ValueError("Boundaries can`t be less than 0")

    if not total_pages > 0:
        raise ValueError("You can`t make pagination with 0 pages")

    if not 1 <= current_page <= total_pages:
        raise ValueError("Your current page is not in range of available pages")

    pages_list = []
    if boundaries >= total_pages // 2:
        pages_list = list([str(page) for page in range(1, total_pages + 1)])
        pages_list = " ".join(pages_list)
        print(pages_list)
        return pages_list
    if boundaries == 0:
        pages_list.insert(0, 1)

    add_pages(pages_list, 1, min(boundaries, total_pages))
    if current_page >= total_pages - boundaries:
        if boundaries < around:
            before_current_page = max(1, current_page - around)
        elif boundaries == around:
            before_current_page = max(1, current_page - boundaries)
        else:
            before_current_page = max(1, current_page - boundaries + 1)
    else:
        before_current_page = max(1, current_page - around)
    if before_current_page > boundaries + 2:
        pages_list.append('...')
    after_current_page = min(total_pages, current_page + around)

    add_pages(pages_list, max(boundaries + 1, before_current_page), after_current_page)

    if after_current_page < total_pages - boundaries - 1:
        pages_list.append('...')

    add_pages(pages_list, max(total_pages - boundaries + 1, after_current_page + 1), total_pages)
    if boundaries == 0 and total_pages not in pages_list:
        pages_list.append(total_pages)

    pages_list = [str(page) for page in pages_list]
    pages_list = " ".join(pages_list)

    print(pages_list)
    return pages_list


if __name__ == "__main__":
    paginate(10, 10, 3, 1)
    paginate(5, 10, 11, 1)
    paginate(1, 10, 6, 1)
    paginate(3, 10, 0, 0)
    paginate(4, 5, 1, 0)
    paginate(6, 11, 1, 2)
    paginate(10, 10, 2, 2)
