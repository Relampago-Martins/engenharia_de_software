import { NoticiaCard } from "@/entities/noticia-card/ui";
import { noticias } from "../lib/noticias-preview";

export function ListaNoticias() {
  return (
    <div className="flex flex-col w-[calc(100%-300px)] px-[2.4%]">
      {noticias.map((noticia) => (
        <NoticiaCard key={noticia.slug} noticia={noticia} />
      ))}
    </div>
  );
}
