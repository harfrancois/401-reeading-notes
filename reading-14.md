# Matplotlib Tutorial

matplotlib is probably the single most used Python package for 2D-graphics. It provides both a very quick way to
visualize data from Python and publication-quality figures in many formats. We are going to explore matplotlib in
interactive mode covering most common cases.

IPython is an enhanced interactive Python shell that has lots of interesting features including named inputs and
outputs, access to shell commands, improved debugging and much more. It allows interactive matplotlib sessions that
have Matlab/Mathematica-like functionality.

pyplot provides a convenient interface to the matplotlib object-oriented plotting library. It is modeled closely
after Matlab(TM). Therefore, the majority of plotting commands in pyplot have Matlab(TM) analogs with similar
arguments. Important commands are explained with interactive examples.

The first step is to get the data for the sine and cosine functions:

    import numpy as np

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)

X is now a NumPy array with 256 values ranging from -π to +π (included). C is the cosine (256 values) and S is the sine (256 values).

To run the example, you can download each of the examples and run it using:

    $ python exercice_1.py

Changing colors and line widths

    plt.figure(figsize=(10,6), dpi=80)
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
    plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-")

Setting limits

    plt.xlim(X.min()*1.1, X.max()*1.1)
    plt.ylim(C.min()*1.1, C.max()*1.1)

Setting ticks

    plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    plt.yticks([-1, 0, +1])

Setting tick labels

    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    
    plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

Moving spines

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

Adding a legend

    t = 2*np.pi/3
    plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.cos(t),], 50, color ='blue')
    
    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
                 xy=(t, np.sin(t)), xycoords='data',
                 xytext=(+10, +30), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    
    plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.sin(t),], 50, color ='red')
    
    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                 xy=(t, np.cos(t)), xycoords='data',
                 xytext=(-90, -50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

