def paginate(current_page: int,
             total_pages: int,
             boundaries: int,
             around: int) -> str:
    args = [current_page, total_pages, boundaries, around]
    if not all(isinstance(arg, int) for arg in args):
        raise TypeError("All arguments must be integers.")

    if not all(arg >= 0 for arg in args):
        raise ValueError("All arguments must be positive integers")

    if not boundaries > 0:
        raise ValueError("You can`t make pagination without at least boundaries of 1")

    if not total_pages > 0:
        raise ValueError("You can`t make pagination with 0 pages")

    if not 1 <= current_page <= total_pages:
        raise ValueError("Your current page is not in range of available pages")

    pages_list = []

    def add_pages(start: int, end: int):
        pages_list.extend(range(start, end + 1))

    add_pages(1, min(boundaries, total_pages))

    before_current_page = max(1, current_page - around)
    if before_current_page > boundaries + 1:
        pages_list.append('...')
    after_current_page = min(total_pages, current_page + around)

    add_pages(max(boundaries + 1, before_current_page), after_current_page)

    if after_current_page < total_pages - boundaries:
        pages_list.append('...')

    add_pages(max(total_pages - boundaries + 1, after_current_page + 1), total_pages)
    pages_list = [str(el) for el in pages_list]
    pages_list = " ".join(pages_list)
    print(pages_list)
    return pages_list


if __name__ == "__main__":
    paginate(3, 10, 2, 2)
