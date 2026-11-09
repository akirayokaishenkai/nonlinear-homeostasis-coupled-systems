import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros estrictos coordinados con el manuscrito "Resource_Agent_Dynamics"
alpha, beta, gamma, delta, x0 = 0.5, 0.2, 0.4, 0.6, 5.0

# Cálculo analítico exacto del Punto Neutro Invariante (Sección III-B)
x_neutro = delta / gamma
y_neutro = (alpha * (x0 - x_neutro)) / (beta * x_neutro)

# Fronteras críticas de extinción y colapso (Sección IV)
p_extincion_agente = (x0, 0.0)    # Agent Extinction Point
p_colapso_fuente = (0.0, 0.0)     # Source Collapse Point

# Dominio temporal para la integración de las ecuaciones diferenciales
t_eval = np.linspace(0, 50, 3000)

def system(t, z, sigma):
    x, y = z
    # Ecuaciones de estado acopladas con operador de paridad direccional (sigma)
    dxdt = sigma * (alpha * (x0 - x) - beta * x * y)
    dydt = sigma * (gamma * x * y - delta * y)
    return [dxdt, dydt]

# Resolución numérica separando los componentes espaciales reales (x, y)
sol_f = solve_ivp(system, (0, 50), [4.5, 1.0], args=(1,), t_eval=t_eval)
sol_i = solve_ivp(system, (0, 50), [1.6, 5.6], args=(-1,), t_eval=t_eval)

# Configuración del entorno gráfico académico
plt.figure(figsize=(8, 6))

# Mapeo de dimensiones: .y para Eje X (Resource), .y para Eje Y (Agent)
plt.plot(sol_f.y[0], sol_f.y[1], 'b-', label='Forward Phase (Growth)', linewidth=2)
plt.plot(sol_i.y[0], sol_i.y[1], 'r--', label='Inverse Phase (Dissipation)', linewidth=2)

# IDENTIFICADORES TOPOLÓGICOS OFICIALES
# 1. El punto fijo no trivial (Coexistencia Dinámica)
plt.plot(x_neutro, y_neutro, 'ko', markersize=10, label=f'Invariant Neutral Point ({x_neutro:.2f}, {y_neutro:.2f})')

# 2. El punto fijo de frontera (Extinción del Agente)
plt.plot(p_extincion_agente[0], p_extincion_agente[1], 'ro', markersize=9, markeredgecolor='black', label=f'Agent Extinction Point ({p_extincion_agente[0]:.1f}, 0)')

# 3. El origen geométrico de colapso (Colapso de la Fuente)
plt.plot(p_colapso_fuente[0], p_colapso_fuente[1], 'X', markersize=9, color='purple', markeredgecolor='black', label='Source Collapse Origin (0,0)')

# Reglas de encuadre para delimitar el primer cuadrante real positivo
plt.axhline(0, color='gray', linewidth=1, linestyle=':')
plt.axvline(0, color='gray', linewidth=1, linestyle=':')

plt.xlim(-0.5, 6)
plt.ylim(-0.5, 8)
plt.xlabel('Resource Potential (x)', fontsize=12)
plt.ylabel('Agent Population Activity (y)', fontsize=12)

# Título unificado con la nueva nomenclatura científica
plt.title('Phase Space Topology: Resource_Agent_Dynamics', fontsize=14)
plt.legend(loc='upper right', fontsize=9)
plt.grid(True, linestyle=':')

# Exportación automática coordinada
plt.savefig('Resource_Agent_Dynamics.png', dpi=300)
plt.show()
