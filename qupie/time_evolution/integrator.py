import numpy as np
from .base import ConstantSampling, BaseHamiltonian


def rk4_unitaries(
        sampler: ConstantSampling,
        hamiltonian: BaseHamiltonian,
        ):
    """
    Solves equation of type 
        d/dt y(t) = -i H y

    Theory
    ------
    Suppose we know have vectors, with equation:
    $$ \dot{\textbf{y}} = M(t) \textbf{y} $$
    or
    $$ \dot{y}_i = \sum_{j} M_{ij}(t) y_i $$

    Then
    $$\textbf{y}_{n+1} = \left(I+ h\frac{L_1+2L_2+2L_3+L_4}{6} \right) \textbf{y}_n = P_n \textbf{y}_n$$
    with
    $$
    \begin{split}
    L_1 &= M(t_n) \\
    L_2 &= M(t_n+h/2) (I+h L_1 /2) \\
    L_3 &= M(t_n+h/2) (I+h L_2/2) \\
    L_4 &= M(t_n+h) (I+h L_3) \\
    \end{split}
    $$

    Check, case when $M(t)=C$, then
    $$
    \begin{split}
    L_1 &= C \\
    L_2 &= (1+h/2)C \\
    L_3 &= (1+h/2+h^2/4)C \\
    L_4 &= (1+h+h^2/2+h^3/4)C \\
    \end{split}
    $$
    and
    $$ P = \left(1+h+h^2/2+h^3/3!+h^4/4! \right) C$$
    """
    times = sampler.get_grid()
    delta = sampler.delta

    identity = np.eye(hamiltonian.dim)[None, :]
    
    k_1 = -1j * hamiltonian.sample(times[:-1])  # shape = (n_times, dim, dim)

    f_a = -1j * hamiltonian.sample(times[:-1] + 0.5 * delta)
    print(f_a.shape, identity.shape, k_1.shape)
    k_2 = f_a @ (identity + k_1 * delta * 0.5) 
    k_3 = f_a @ (identity + k_2 * delta * 0.5)

    f_b = -1j * hamiltonian.sample(times[1:])
    k_4 = f_b @ (identity + k_3 * delta)

    return identity + (k_1 + 2 * k_2 + 2 * k_3 + k_4) * delta / 6


def propagate(initial_state, unitaries):
    evo_states = [initial_state]
    for u in unitaries:
        evo_states.append(u @ evo_states[-1])
    return np.array(evo_states)