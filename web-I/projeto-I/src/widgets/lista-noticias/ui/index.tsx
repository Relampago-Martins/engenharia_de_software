import { NoticiaCard } from "@/entities/noticia-card/ui";
import { getNoticiasPreview } from "@/shared/lib/noticias";

export function ListaNoticias() {
  const noticias = getNoticiasPreview();
  return (
    <div className="flex flex-col w-[calc(100%-300px)] px-[2.4%]">
      {noticias.map((noticia) => (
        <NoticiaCard key={noticia.slug} noticia={noticia} />
      ))}
    </div>
  );
}
