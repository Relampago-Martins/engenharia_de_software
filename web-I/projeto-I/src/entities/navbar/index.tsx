import { cn } from "@/shared/lib/utils";
import { Button } from "@/shared/ui/button";
import { Link } from "react-router-dom";

type NavBarProps = {
  children: React.ReactNode;
  className?: string;
};

export function NavBar({ children, className }: NavBarProps) {
  return (
    <nav>
      <ul className={cn("flex items-center", className)}>{children}</ul>
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
    <li className="leading-[46px]">
      <Button variant={"ghost"} className="text-[15px] py-0 px-[20px]">
        <Link to={href} className="text-muted font-semibold">
          {children}
        </Link>
      </Button>
    </li>
  );
}
