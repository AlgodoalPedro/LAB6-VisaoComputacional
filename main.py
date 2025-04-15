import math
import numpy as np
import cv2
import matplotlib.pyplot as plt


################################################################################################################################################################################


def processar_imagem(nome_imagem, parametros):
    """
    Processa a imagem com base nos parâmetros fornecidos.
    
    :param nome_imagem: Nome do arquivo da imagem.
    :param parametros: Dicionário com os parâmetros específicos para a análise.
    """
    img = cv2.imread(nome_imagem)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    a = img_gray.max()

    limiar_binarizacao = parametros['limiar_binarizacao'](a) if callable(parametros['limiar_binarizacao']) else parametros['limiar_binarizacao'] * a

    _, thresh = cv2.threshold(
        img_gray, 
        limiar_binarizacao, 
        a, 
        cv2.THRESH_BINARY_INV
    )

    tamanhoKernel = parametros['tamanho_kernel']
    kernel = np.ones((tamanhoKernel, tamanhoKernel), np.uint8)

    if parametros.get('usar_morfologia', False):
        img_close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
        img_dilate = cv2.dilate(img_close, kernel, iterations=2)
        img_open = cv2.morphologyEx(img_dilate, cv2.MORPH_OPEN, kernel, iterations=1)
        thresh_open = img_open
    else:
        thresh_open = thresh

    img_blur = cv2.blur(img_gray, ksize=(tamanhoKernel, tamanhoKernel))

    edges_gray = cv2.Canny(
        image=img_gray, 
        threshold1=parametros['canny_threshold1'] * a, 
        threshold2=parametros['canny_threshold2'] * a
    )
    edges_blur = cv2.Canny(
        image=img_blur, 
        threshold1=parametros['canny_threshold1'] * a, 
        threshold2=parametros['canny_threshold2'] * a
    )

    contours, _ = cv2.findContours(
        image=thresh_open,
        mode=cv2.RETR_EXTERNAL if parametros.get('usar_morfologia', False) else cv2.RETR_TREE,
        method=cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    img_copy = img.copy()

    if 'area_min' in parametros and 'area_max' in parametros and parametros['area_min'] is not None and parametros['area_max'] is not None:
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if parametros['area_min'] < area < parametros['area_max']:
                cv2.drawContours(img_copy, [cnt], -1, (255, 0, 0), 2)
    else:
        cv2.drawContours(img_copy, contours, -1, (255, 0, 0), 2)

    final = img_copy.copy()

    imagens = [img, img_blur, img_gray, edges_gray, edges_blur, thresh, thresh_open, final]
    formatoX = math.ceil(len(imagens) ** 0.5)
    formatoY = formatoX if (formatoX ** 2 - len(imagens)) <= formatoX else formatoX - 1

    plt.figure(figsize=(18, 12))
    for i in range(len(imagens)):
        plt.subplot(formatoY, formatoX, i + 1)
        plt.imshow(imagens[i], cmap='gray' if len(imagens[i].shape) == 2 else None)
        plt.xticks([]), plt.yticks([])

    pasta_saida = nome_imagem.split('/')[0]
    plt.tight_layout()
    plt.savefig(f'./passoapasso_{nome_imagem.split("/")[-1].split(".")[0].lower()}.png', dpi=300, bbox_inches='tight')
    plt.show()

    output_path = f'./final_{nome_imagem.split("/")[-1].split(".")[0].lower()}.png'
    cv2.imwrite(output_path, cv2.cvtColor(final, cv2.COLOR_RGB2BGR))


################################################################################################################################################################################


processar_imagem(r'GIRAFA.jpeg', parametros = {
    'limiar_binarizacao': 10,
    'tamanho_kernel': 5,
    'canny_threshold1': 0.5,
    'canny_threshold2': 0.5,
    'area_min': None,
    'area_max': None
})

processar_imagem(r'Aviao.jpeg', parametros = {
    'limiar_binarizacao': 0.4,
    'tamanho_kernel': 5,
    'canny_threshold1': 0.5,
    'canny_threshold2': 0.5,
    'area_min': 5000,
    'area_max': 100000,
    'usar_morfologia': True
})

processar_imagem(r'Satelite.jpeg', parametros = {
    'limiar_binarizacao': lambda a: (a * 50) * 0.3,
    'tamanho_kernel': 5,
    'canny_threshold1': 0.5,
    'canny_threshold2': 0.5,
    'area_min': 500,
    'area_max': 20000
})