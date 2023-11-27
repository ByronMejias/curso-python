import matplotlib.pyplot as plot

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    value = [100, 50, 160, 20]

    fix, ax = plot.subplots()
    ax.pie(value, labels=labels)
    plot.savefig('pie.png')
    plot.close()
