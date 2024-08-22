import { Cabecalho } from "@/entities/cabecalho";
import { NavBar, NavBarLink } from "@/entities/navbar";

export function HackerNewsPage() {
  return (
    <div className="flex flex-col h-svh w-svw ">
      <div className="bg-header-gradient w-100">
        <Cabecalho />
      </div>
      <NavBar>
        <NavBarLink href="#home">Home</NavBarLink>
        <NavBarLink href="#cyber-attacks">Cyber Attacks</NavBarLink>
        <NavBarLink href="#vulnerabilities">Vulnerabilities</NavBarLink>
        <NavBarLink href="#store">Store</NavBarLink>
        <NavBarLink href="#contact">Contact</NavBarLink>
      </NavBar>
    </div>
  );
}
