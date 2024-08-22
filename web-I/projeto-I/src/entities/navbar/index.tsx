import { cn } from "@/shared/lib/utils";
import { Link } from "react-router-dom";

type NavBarProps = {
  children: React.ReactNode;
  className?: string;
};

export function NavBar({ children, className }: NavBarProps) {
  return (
    <nav className="border-b-2 border-b-border bg-white clearfix h-[46px]">
      <ul
        className={cn("list-none clearfix mx-auto max-w-[1110px]", className)}
      >
        {children}
      </ul>
    </nav>
  );
}

export function NavBarLink({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) {
  return (
    <li className="leading-[46px] h-[46px] border-b-4 border-b-transparent hover:border-b-primary float-left px-[20px]">
      <Link
        to={href}
        className="text-muted font-semibold hover:text-muted tracking-[.3px] text-[15px]"
      >
        {children}
      </Link>
    </li>
  );
}
