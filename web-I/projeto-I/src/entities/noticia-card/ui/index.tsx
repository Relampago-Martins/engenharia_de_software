import { Card, CardContent } from "@/shared/ui/card";
import { faCalendarAlt } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";
import { NoticiaPreview } from "../lib/types";
import { date2String } from "../lib/utils";

export function NoticiaCard({ noticia }: { noticia: NoticiaPreview }) {
  return (
    <Link to={`/noticias/${noticia.slug}`}>
      <Card className="mb-[20px] border-none shadow-none">
        <CardContent className="flex gap-4">
          <div className="w-2/5 rounded-[10px] overflow-hidden hover:rounded-none transition-all duration-300 shrink-0">
            <img
              src={noticia.urlCapa}
              alt={noticia.titulo}
              width={728}
              className="hover:scale-105 transition-all duration-300"
            />
          </div>
          <div className="flex flex-col">
            <h1 className="text-foreground hover:underline text-[17px] leading-[28.05px] font-bold">
              {noticia.titulo}
            </h1>
            <div className="flex items-center text-gray-500 text-xs gap-2">
              <FontAwesomeIcon icon={faCalendarAlt} />
              {date2String(noticia.dataPublicacao)}
            </div>
          </div>
        </CardContent>
      </Card>
    </Link>
  );
}
