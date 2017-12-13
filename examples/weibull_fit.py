import weibull

# fail times include no censored data
fail_times = [
    9402.7,
    6082.4,
    13367.2,
    10644.6,
    8632.0,
    3043.4,
    12860.2,
    1034.5,
    2550.9,
    3637.1
]


# this is where the actual analysis occurs
analysis = weibull.Analysis(fail_times)
analysis.plot()

print(f'beta: {analysis.beta}\teta: {analysis.eta}')
