import { Button } from "@/shared/ui/button";
import { ClickImage } from "@/shared/ui/click-imagem";
import hackerNews from "../../assets/hacker-news.png";

export function HackerNewsPage() {
  return (
    <div className="flex flex-col h-svh w-svw">
      <div className="bg-primary w-100">
        <div className="flex justify-between items-center mx-auto max-w-[1110px] px-5">
          <ClickImage
            href="/"
            src={hackerNews}
            className="object-contain w-[425px]"
            alt="Hacker News logo"
          />
          <Button variant={"subscribe"}>Subscribe - Get Latest News</Button>
        </div>
      </div>
    </div>
  );
}
