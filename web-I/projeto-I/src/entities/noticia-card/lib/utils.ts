/**
 * Recebe uma data e retorna uma string no formato month day, year
 * @param date 
 */
export function date2String(date: Date): string {
    return date.toLocaleDateString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric",
    });
  
}