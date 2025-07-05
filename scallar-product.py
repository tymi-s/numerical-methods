from scipy import integrate

def iloczyn_skalarny(f, g, a, b):

    integrand = lambda x: f(x) * g(x)
    result, _ = integrate.quad(integrand, a, b)
    return result