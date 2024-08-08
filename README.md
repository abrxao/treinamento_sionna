## Demandas

#### Tarefa 2

- [ ] Usar posição de antena real para construir a cena
- [ ] Calcular a resposta ao Impulso do Canal (paths.cir())
- [ ] Plotar gráficos resposta usando _a_ e _$\tau$_
- [ ] Calcular a resposta na frequencia do canal usando

```
20*np.log10(tf.abs(h_f).numpy()) #Tranformando em DB
subcarrier_frequencies(num_subcarriers, subcarrier_spacing) #Gerando frequencias de uso do sistema
```

- [ ] Escolher valores para calcular resposta na frequencia do site abaixo
      [NR Explained](https://www.nrexplained.com/bandwidth)
- [ ] Plotar gráficos da resposta na frequência do usuário usando _cir_to_ofdm_channel()_
- [ ] Pesquisar referências sobre OFDM

#### Tarefa 1 - Concluida

- [x] Escolher a região de simulação. (-38.51023,-3.72479,-38.50522,-3.72078)
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
