import { Card, CardContent } from "@/shared/ui/card";
import { Link } from "react-router-dom";
import { NoticiaPreview } from "../lib/types";

export function NoticiaCard({ noticia }: { noticia: NoticiaPreview }) {
  return (
    <Link to={`/noticias/${noticia.slug}`}>
      <Card className="mb-[20px] border-none shadow-none">
        <CardContent className="flex gap-4">
          <div className="w-2/5 rounded-[10px] overflow-hidden hover:rounded-none transition-all duration-300">
            <img
              src={noticia.urlCapa}
              alt={noticia.titulo}
              width={728}
              className="hover:scale-105 transition-all duration-300"
            />
          </div>
          <h1>{noticia.titulo}</h1>
        </CardContent>
      </Card>
    </Link>
  );
}
