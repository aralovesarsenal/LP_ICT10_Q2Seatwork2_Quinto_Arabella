from pyscript import display, document


def calculate_gwa(*_args):
    """Simple GWA calculator called from the HTML button via py-click.

    Reads the six grade inputs, validates them, computes the average and displays
    the result into the element with id 'gwaResult'.
    """
    ids = ['sci', 'eng', 'ict', 'math', 'fil', 'pe']
    grades = []

    for i in ids:
        el = document.getElementById(i)
        if el is None:
            display(f"Missing input: {i}", target="gwaResult")
            return
        val = el.value.strip()
        if val == "":
            display("Please fill in all grade fields.", target="gwaResult")
            return
        try:
            g = float(val.replace(',', '.'))
        except Exception:
            display(f"Invalid grade for {i}: {val}", target="gwaResult")
            return
        if g < 0 or g > 100:
            display("Grades must be between 0 and 100.", target="gwaResult")
            return
        grades.append(g)

    avg = sum(grades) / len(grades)

    if avg >= 90:
        remark = 'Excellent'
    elif avg >= 80:
        remark = 'Very Good'
    elif avg >= 70:
        remark = 'Satisfactory'
    elif avg >= 60:
        remark = 'Fair'
    else:
        remark = 'Needs Improvement'

    first = document.getElementById('first')
    last = document.getElementById('last')
    name = ' '.join([(first.value.strip() if first else ''), (last.value.strip() if last else '')]).strip() or 'Unnamed student'

    display(f"<strong>{name}</strong> — GWA: <strong>{avg:.2f}</strong> ({remark})", target="gwaResult")
