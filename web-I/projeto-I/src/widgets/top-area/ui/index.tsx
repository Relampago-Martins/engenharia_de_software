"use client";
import { Cabecalho } from "@/entities/cabecalho";
import { NavBar, NavBarLink } from "@/entities/navbar";
import { Input } from "@/shared/ui/input";
import { faBars, faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useState } from "react";

export function TopArea() {
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  return (
    <>
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
          <button
            className="px-6"
            onClick={() => setIsSearchOpen((val) => !val)}
          >
            <FontAwesomeIcon
              icon={faSearch}
              className="text-muted text-xl ml-[10px]"
            />
          </button>
          <div className="px-6">
            <FontAwesomeIcon
              icon={faBars}
              className="text-muted text-xl ml-[10px]"
            />
          </div>
        </div>
      </NavBar>
      {isSearchOpen && (
        <div className="px-[20px] py-[10px]">
          <Input type="text" placeholder="Search Here..." />
        </div>
      )}
    </>
  );
}
