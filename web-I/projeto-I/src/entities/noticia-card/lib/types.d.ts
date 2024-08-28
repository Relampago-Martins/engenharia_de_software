export type Noticia = {
    slug: string;
    urlCapa: string;
    titulo: string;
    dataPublicacao: date;
    tag: string;
    resumo: string;
    autor: string;
}

export type NoticiaPreview = Pick<Noticia, 
    'slug' | 'urlCapa' | 'titulo' | 'dataPublicacao' | 'tag' | 'resumo'>;