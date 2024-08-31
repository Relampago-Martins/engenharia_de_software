import { ListaNoticias } from "@/widgets/lista-noticias/ui";
import { TopArea } from "@/widgets/top-area/ui";

export function HackerNewsPage() {
  return (
    <div className="flex flex-col h-svh w-svw ">
      <TopArea />
      <div className="flex flex-row mt-10">
        <ListaNoticias />
      </div>
    </div>
  );
}
