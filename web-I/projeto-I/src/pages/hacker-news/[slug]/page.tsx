import { date2String } from "@/entities/noticia-card/lib/utils";
import { getNoticiaBySlug } from "@/shared/lib/noticias";
import { Noticia } from "@/shared/lib/types";
import { TopArea } from "@/widgets/top-area/ui";
import { faCalendarAlt } from "@fortawesome/free-regular-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useParams } from "react-router-dom";

export function NoticiaDetailPage() {
  const { slug } = useParams<{ slug: string }>();
  const noticia: Noticia | undefined = getNoticiaBySlug(slug || "");

  if (!noticia) {
    return <div>Notícia não encontrada</div>;
  }

  return (
    <div className="flex flex-col h-svh w-svw ">
      <TopArea />
      <main className="max-w-[766px] md:max-w-[1110px] m-auto">
        <div className="flex flex-col mt-10">
          <h1 className="text-foreground font-black text-[32px] px-[20px]">
            {noticia.titulo}
          </h1>
          <div className="px-[20px] flex flex-col">
            <div className="flex justify-between leading-[40px] text-[13px]">
              <div className="flex gap-3">
                <div className="flex items-center gap-2">
                  <FontAwesomeIcon icon={faCalendarAlt} />
                  <div>{date2String(noticia.dataPublicacao)}</div>
                </div>
                <div className="flex gap-1 items-center">
                  <FontAwesomeIcon icon={faUser} />
                  <div>{noticia.autor}</div>
                </div>
              </div>
              <div>{noticia.tags.join(" / ")}</div>
            </div>
            <img
              src={noticia.urlCapa}
              alt={noticia.titulo}
              className="rounded-[10px]"
            />
            <div>{noticia.resumo}</div>
            {noticia.paragrafos.map((paragrafo, index) => (
              <p key={index}>{paragrafo}</p>
            ))}
          </div>
        </div>
      </main>
    </div>
  );
}
