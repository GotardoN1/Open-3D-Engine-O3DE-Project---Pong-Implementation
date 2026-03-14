import azlmbr.object as az_object
import azlmbr.math as az_math
import azlmbr.bus as az_bus

# Simulação de um componente de controle para o Paddle no O3DE
class PaddleController:
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.speed = 5.0

    def on_update(self, delta_time, input_value):
        """
        Atualiza a posição vertical do Paddle com base no input.
        """
        # Obtém a transformação atual da entidade
        current_tm = az_bus.TransformBus(az_bus.GET_WORLD_TM, self.entity_id)
        pos = current_tm.get_translation()

        # Calcula o novo deslocamento (Eixo Z no O3DE costuma ser o vertical)
        new_z = pos.z + (input_value * self.speed * delta_time)
        
        # Limita o movimento para não sair da tela (Bounds)
        new_z = max(-10.0, min(10.0, new_z))
        
        pos.z = new_z
        current_tm.set_translation(pos)
        
        # Envia de volta para o motor
        az_bus.TransformBus(az_bus.SET_WORLD_TM, self.entity_id, current_tm)

print("Sistema de Paddle carregado com sucesso.")
