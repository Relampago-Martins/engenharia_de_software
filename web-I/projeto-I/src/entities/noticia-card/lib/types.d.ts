export type Noticia = {
    slug: string;
    urlCapa: string;
    titulo: string;
    dataPublicacao: date;

}

export type NoticiaPreview = Pick<Noticia, 'slug' | 'urlCapa' | 'titulo'>;