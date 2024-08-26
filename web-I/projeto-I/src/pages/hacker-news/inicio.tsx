import { Cabecalho } from "@/entities/cabecalho";
import { NavBar, NavBarLink } from "@/entities/navbar";
import { faBars, faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

export function HackerNewsPage() {
  return (
    <div className="flex flex-col h-svh w-svw ">
      <div className="bg-header-gradient w-100">
        <Cabecalho />
      </div>
      <NavBar className="flex">
        <div className="flex items-center mr-auto">
          <NavBarLink href="#home">Home</NavBarLink>
          <NavBarLink href="#cyber-attacks">Cyber Attacks</NavBarLink>
          <NavBarLink href="#vulnerabilities">Vulnerabilities</NavBarLink>
          <NavBarLink href="#store">Store</NavBarLink>
          <NavBarLink href="#contact">Contact</NavBarLink>
        </div>
        <div className="flex items-center">
          <FontAwesomeIcon icon={faSearch} className="text-muted" />
          <FontAwesomeIcon icon={faBars} className="text-muted" />
        </div>
      </NavBar>
    </div>
  );
}
