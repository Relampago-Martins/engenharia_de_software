import hackerNews from "@/assets/hacker-news.png";
import { Button } from "@/shared/ui/button";
import { ClickImage } from "@/shared/ui/click-imagem";
import { faEnvelope } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";

export function Cabecalho({}) {
  return (
    <header className="bg-header-gradient w-100">
      <div className="flex justify-between items-center mx-auto max-w-[1110px] px-5">
        <div className="w-1/2">
          <ClickImage
            href="/"
            src={hackerNews}
            className="object-contain w-[425px] max-w-full"
            alt="Hacker News logo"
          />
        </div>
        <Link to="#email">
          <Button variant={"subscribe"} className="gap-2 my-[18.5px] ">
            <FontAwesomeIcon icon={faEnvelope} />
            Subscribe – Get Latest News
          </Button>
        </Link>
      </div>
    </header>
  );
}
