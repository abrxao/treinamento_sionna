## Demandas

#### Tarefa 5

- [ ] Rescolher area de estudo para que estradas não fiquem cortadas na cena. (coordenadas)
- [ ] Gerar arquivos com camera posicionada e usuarios se movendo.
- [ ] Pegar diferença de localização do sumo e sionna para ajustar posição da simulação.
- [ ] Gerar gif a partir de imagens de movimentação.
- [ ] Pesquisar referências sobre OFDM

#### Tarefa 4

- [x] Usar as coordenadas do blender no sumo para gerar simulação
- [x] Instalar o sumo e fazer uma simulação na região escolhida da tarefa 1.
- [x] Encontrar a pasta com os arquivos da simulação. (Road-Types: Highway) (Vehicles: Cars[50 , 12]) (Duration: 100)
- [x] Adicionar simulação do local escolhido a pasta "sumo_simulations"

#### Tarefa 3

- [x] Posicionar câmera em local de movimentação
- [x] Tentar adicionar movimentação manualmente. [Sionna com Mobilidade](https://nvlabs.github.io/sionna/examples/Sionna_Ray_Tracing_Mobility.html)

#### Tarefa 2

- [x] Usar posição de antena real para construir a cena (CONDOMÍNIO EDIFÍCIO NAUTILUS, AVENIDA BEIRA MAR)
- [x] Calcular a resposta ao Impulso do Canal (paths.cir())
- [x] Plotar gráficos resposta usando _a_ e _$\tau$_
- [x] Calcular a resposta na frequencia do canal usando

```
20*np.log10(tf.abs(h_f).numpy()) #Tranformando em DB
subcarrier_frequencies(num_subcarriers, subcarrier_spacing) #Gerando frequencias de uso do sistema
```

- [x] Escolher valores para calcular resposta na frequencia do site abaixo
      [NR Explained](https://www.nrexplained.com/bandwidth)
- [x] Plotar gráficos da resposta na frequência do usuário usando _cir_to_ofdm_channel()_
- [x] Pesquisar referências sobre OFDM

#### Tarefa 1 - Concluida

- [x] Escolher a região de simulação. (-38.51233,-3.72236,-38.50909,-3.72018)
- [x] Salvar a posição da antena escolhida. (Se possivel justificar a escolha).
- [x] Colocar no minimo dois receptores na cena em posições reais.
- [x] Usar o scene.preview() para ver a posição no mapa e encontra-los.
- [x] Usar o scene.coverage_map() para ver o cm.
- [x] Calcular os caminhos dos raios usando o codigo abaixos

```
paths = scene.compute_paths(diffraction=True,
                                max_depth=3)
```

- [x] Renderizar os caminhos com um novo scene.preview()
